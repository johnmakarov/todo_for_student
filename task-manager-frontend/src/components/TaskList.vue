<template>
  <div class="space-y-4">
    <div v-if="loading && tasks.length === 0" class="text-center py-8">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
      <p class="text-gray-500 mt-2">Загрузка задач...</p>
    </div>
    
    <div v-else-if="tasks.length === 0" class="text-center py-8">
      <div class="text-gray-400 mb-4">
        <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
        </svg>
      </div>
      <p class="text-gray-500 text-lg">Задачи не найдены</p>
      <p class="text-gray-400 text-sm mt-1">Добавьте первую задачу выше</p>
    </div>
    
    <div v-else class="space-y-3">
      <TaskItem
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        :loading="loading"
        @complete="$emit('complete-task', $event)"
        @delete="$emit('delete-task', $event)"
      />
    </div>
  </div>
</template>

<script setup>
import TaskItem from './TaskItem.vue'

defineProps({
  tasks: Array,
  loading: Boolean
})

defineEmits(['complete-task', 'delete-task'])
</script>