import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const taskAPI = {
  // Получить все задачи
  getAllTasks: () => api.get('/tasks/'),
  
  // Получить задачу по ID
  getTaskById: (id) => api.get(`/tasks/${id}`),
  
  // Создать задачу
  createTask: (description) => api.post('/tasks/', { description }),
  
  // Отметить задачу выполненной
  completeTask: (id) => api.patch(`/tasks/${id}/complete`),
  
  // Удалить задачу
  deleteTask: (id) => api.delete(`/tasks/${id}`),
  
  // Получить выполненные задачи
  getCompletedTasks: () => api.get('/tasks/status/completed'),
  
  // Получить невыполненные задачи
  getPendingTasks: () => api.get('/tasks/status/pending'),
  
  // Очистить все задачи
  clearAllTasks: () => api.delete('/tasks/'),
  
  // Получить статистику
  getStats: () => api.get('/stats/'),
}

export default api