<template>
  <form @submit.prevent="handleSubmit" class="mb-8">
    <div class="flex gap-4">
      <input
        v-model="newTask"
        type="text"
        placeholder="Добавьте новую задачу..."
        class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition-all duration-200 shadow-sm"
        :disabled="loading"
      />
      <button
        type="submit"
        :disabled="loading || !newTask.trim()"
        class="px-6 py-3 bg-primary-600 text-white font-medium rounded-lg hover:bg-primary-700 focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-md"
      >
        <span v-if="loading" class="flex items-center">
          <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Добавление...
        </span>
        <span v-else>Добавить</span>
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  loading: Boolean
})

const emit = defineEmits(['add-task'])

const newTask = ref('')

const handleSubmit = () => {
  if (newTask.value.trim()) {
    emit('add-task', newTask.value)
    newTask.value = ''
  }
}
</script>