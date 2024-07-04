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
        # Create a comment in the database first (assuming it's empty for this test)
        new_comment = Comment(name="Test User", content="This is a test comment")
        self.db.add(new_comment)
        self.db.commit()

        # Test retrieving the comment
        response = self.client.get("/api/comment/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"
        assert response.json()["content"] == "This is a test comment"
    def test_get_comment(self):
        comment = create_comment("This is a test comment", self.db)
        self.comments_to_delete.append(comment.id)
        fetched_comment = get_comment(comment.id, self.db)
        self.assertEqual(fetched_comment.id, comment.id)
        self.assertEqual(fetched_comment.content, comment.content)

    def test_update_comment(self):
        # Create a comment in the database first (assuming it's empty for this test)
        new_comment = Comment(name="Test User", content="This is a test comment")
        self.db.add(new_comment)
        self.db.commit()

        # Test updating the comment
        update_data = {"content": "Updated test comment"}
        response = self.client.put("/api/update/1", json=update_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"
        assert response.json()["content"] == "Updated test comment"

        # Verify the comment was updated
        response = self.client.get("/api/comment/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"
        assert response.json()["content"] == "Updated test comment"

    def test_update_comment(self):
        comment = create_comment("Original Comment", self.db)
        self.comments_to_delete.append(comment.id)
        updated_comment = update_comment(comment.id, "Updated Comment", self.db)
        self.assertEqual(updated_comment.content, "Updated Comment")

    def test_delete_comment(self):
        # Create a comment in the database first (assuming it's empty for this test)
        new_comment = Comment(name="Test User", content="This is a test comment")
        self.db.add(new_comment)
        self.db.commit()

        # Test deleting the comment
        response = self.client.delete("/api/delete/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"
        assert response.json()["content"] == "This is a test comment"

        # Verify the comment was actually deleted
        response = self.client.get("/api/comment/1")
        assert response.status_code == 404  # Assuming 404 is returned for non-existent resources



if __name__ == '__main__':
    unittest.main()
