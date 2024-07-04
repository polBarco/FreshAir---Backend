import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Comment, create_comment, get_comment, get_comments, update_comment, delete_comment

DATABASE_URL = "sqlite:///:memory:"


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.db = self.Session()
        self.comments_to_delete = []

    def tearDown(self):
        # Clean up comments created during the tests
        for comment_id in self.comments_to_delete:
            delete_comment(comment_id, self.db)
        self.db.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def test_create_comment(self):
        comment = create_comment("This is a test comment", self.db)
        self.assertIsNotNone(comment.id)
        self.assertEqual(comment.content, "This is a test comment")
        self.comments_to_delete.append(comment.id)

    def test_get_comment(self):
        comment = create_comment("This is a test comment", self.db)
        self.comments_to_delete.append(comment.id)
        fetched_comment = get_comment(comment.id, self.db)
        self.assertEqual(fetched_comment.id, comment.id)
        self.assertEqual(fetched_comment.content, comment.content)

    def test_get_comments(self):
        comment1 = create_comment("Comment 1", self.db)
        comment2 = create_comment("Comment 2", self.db)
        self.comments_to_delete.append(comment1.id)
        self.comments_to_delete.append(comment2.id)
        comments = get_comments(db_session=self.db)
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[0].content, "Comment 1")
        self.assertEqual(comments[1].content, "Comment 2")

    def test_update_comment(self):
        comment = create_comment("Original Comment", self.db)
        self.comments_to_delete.append(comment.id)
        updated_comment = update_comment(comment.id, "Updated Comment", self.db)
        self.assertEqual(updated_comment.content, "Updated Comment")

    def test_delete_comment(self):
        comment = create_comment("Comment to be deleted", self.db)
        delete_success = delete_comment(comment.id, self.db)
        self.assertTrue(delete_success)
        deleted_comment = get_comment(comment.id, self.db)
        self.assertIsNone(deleted_comment)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
