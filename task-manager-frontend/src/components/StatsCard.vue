<template>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
    <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
      <div class="text-2xl font-bold text-gray-900">{{ stats.total_tasks }}</div>
      <div class="text-sm text-gray-500 mt-1">Всего задач</div>
    </div>
    
    <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
      <div class="text-2xl font-bold text-green-600">{{ stats.completed_tasks }}</div>
      <div class="text-sm text-gray-500 mt-1">Выполнено</div>
    </div>
    
    <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
      <div class="text-2xl font-bold text-orange-600">{{ stats.pending_tasks }}</div>
      <div class="text-sm text-gray-500 mt-1">В процессе</div>
    </div>
    
    <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
      <div class="text-2xl font-bold text-primary-600">{{ stats.completion_rate }}%</div>
      <div class="text-sm text-gray-500 mt-1">Прогресс</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  stats: Object
})
</script>