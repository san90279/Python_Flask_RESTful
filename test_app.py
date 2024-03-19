import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        
    
    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        task_data = {"text": "create task"}
        response = self.client.post('/task', json=task_data)
        self.assertEqual(response.status_code, 201)

    def test_update_task(self):
        self.client.get('/tasks')
        task_data = {"text": "update task","status": 1,"id": 1}
        response = self.client.put('/task/1', json=task_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        response = self.client.delete('/task/1')
        self.assertEqual(response.status_code, 200)        

if __name__ == '__main__':
    unittest.main()
