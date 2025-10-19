<template>
  <div class="app">
    <div class="container">
      <!-- Заголовок -->
      <header class="text-center mb-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">
          📝 Менеджер задач
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
          Организуйте свои задачи эффективно и красиво
        </p>
      </header>

      <!-- Основной контент -->
      <main class="card p-6 md-p-8">
        <!-- Форма добавления задачи -->
        <TaskForm
          :loading="loading"
          @add-task="handleAddTask"
        />

        <!-- Фильтры и управление -->
        <div class="flex flex-wrap gap-4 items-center justify-between mb-6">
          <div class="filter-buttons">
            <button
              v-for="filterOption in filterOptions"
              :key="filterOption.value"
              @click="filter = filterOption.value"
              class="filter-btn"
              :class="{ active: filter === filterOption.value }"
            >
              {{ filterOption.label }}
            </button>
          </div>

          <button
            v-if="allTasks.length > 0"
            @click="handleClearAll"
            :disabled="loading"
            class="btn btn-danger"
          >
            Очистить все
          </button>
        </div>

        <!-- Статистика -->
        <StatsCard :stats="stats" />

        <!-- Список задач -->
        <TaskList
          :tasks="tasks"
          :loading="loading"
          @complete-task="handleCompleteTask"
          @delete-task="handleDeleteTask"
        />

        <!-- Ошибки -->
        <div
          v-if="error"
          class="alert alert-error"
        >
          {{ error }}
        </div>
      </main>

      <!-- Футер -->
      <footer class="text-center mt-8 text-gray-500 text-sm">
        Создано с помощью Vue 3 & FastAPI
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useTasks } from './composables/useTasks'
import { taskAPI } from './services/api'
import TaskForm from './components/TaskForm.vue'
import TaskList from './components/TaskList.vue'
import StatsCard from './components/StatsCard.vue'

const { 
  tasks, 
  allTasks,
  loading, 
  error, 
  filter,
  loadTasks, 
  addTask, 
  completeTask, 
  deleteTask, 
  clearAllTasks 
} = useTasks()

const stats = ref({
  total_tasks: 0,
  completed_tasks: 0,
  pending_tasks: 0,
  completion_rate: 0
})

const filterOptions = [
  { label: 'Все задачи', value: 'all' },
  { label: 'В процессе', value: 'pending' },
  { label: 'Выполненные', value: 'completed' }
]

// Загрузка статистики
const loadStats = async () => {
  try {
    const response = await taskAPI.getStats()
    stats.value = response.data
  } catch (err) {
    console.error('Error loading stats:', err)
  }
}

// Обработчики событий
const handleAddTask = async (description) => {
  await addTask(description)
  await loadStats()
}

const handleCompleteTask = async (id) => {
  await completeTask(id)
  await loadStats()
}

const handleDeleteTask = async (id) => {
  await deleteTask(id)
  await loadStats()
}

const handleClearAll = async () => {
  if (confirm('Вы уверены, что хотите удалить все задачи?')) {
    await clearAllTasks()
    await loadStats()
  }
}

// Загрузка данных при монтировании
onMounted(async () => {
  await loadTasks()
  await loadStats()
})

// Обновление статистики при изменении фильтра или задач
watch([tasks, filter], loadStats)
</script>

<style scoped>
.app {
  min-height: 100vh;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0e7ff 100%);
  padding: 2rem 0;
}

@media (max-width: 768px) {
  .app {
    padding: 1rem 0;
  }
}
</style>