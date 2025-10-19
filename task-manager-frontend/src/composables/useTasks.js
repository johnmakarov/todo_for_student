import { ref, computed } from 'vue'
import { taskAPI } from '../services/api'

export function useTasks() {
  const tasks = ref([])
  const loading = ref(false)
  const error = ref(null)
  const filter = ref('all') // 'all', 'pending', 'completed'

  // Отфильтрованные задачи
  const filteredTasks = computed(() => {
    switch (filter.value) {
      case 'completed':
        return tasks.value.filter(task => task.completed)
      case 'pending':
        return tasks.value.filter(task => !task.completed)
      default:
        return tasks.value
    }
  })

  // Загрузка всех задач
  const loadTasks = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await taskAPI.getAllTasks()
      tasks.value = response.data
    } catch (err) {
      error.value = 'Ошибка при загрузке задач'
      console.error('Error loading tasks:', err)
    } finally {
      loading.value = false
    }
  }

  // Добавление задачи
  const addTask = async (description) => {
    if (!description.trim()) return
    
    loading.value = true
    error.value = null
    try {
      const response = await taskAPI.createTask(description.trim())
      tasks.value.push(response.data)
      await loadTasks() // Перезагружаем для актуальных данных
    } catch (err) {
      error.value = 'Ошибка при добавлении задачи'
      console.error('Error adding task:', err)
    } finally {
      loading.value = false
    }
  }

  // Отметка задачи выполненной
  const completeTask = async (id) => {
    loading.value = true
    error.value = null
    try {
      await taskAPI.completeTask(id)
      const task = tasks.value.find(t => t.id === id)
      if (task) {
        task.completed = true
      }
    } catch (err) {
      error.value = 'Ошибка при обновлении задачи'
      console.error('Error completing task:', err)
    } finally {
      loading.value = false
    }
  }

  // Удаление задачи
  const deleteTask = async (id) => {
    loading.value = true
    error.value = null
    try {
      await taskAPI.deleteTask(id)
      tasks.value = tasks.value.filter(task => task.id !== id)
    } catch (err) {
      error.value = 'Ошибка при удалении задачи'
      console.error('Error deleting task:', err)
    } finally {
      loading.value = false
    }
  }

  // Очистка всех задач
  const clearAllTasks = async () => {
    loading.value = true
    error.value = null
    try {
      await taskAPI.clearAllTasks()
      tasks.value = []
    } catch (err) {
      error.value = 'Ошибка при очистке задач'
      console.error('Error clearing tasks:', err)
    } finally {
      loading.value = false
    }
  }

  return {
    tasks: filteredTasks,
    allTasks: tasks,
    loading,
    error,
    filter,
    loadTasks,
    addTask,
    completeTask,
    deleteTask,
    clearAllTasks,
  }
}