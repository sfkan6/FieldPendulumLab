<script setup>
import { Table, Button, Form } from '@/shared/ui'
import { getTableHeaderByDataType } from '@/shared/config'


const { dataType, dataSample, tableHeight } = defineProps({
  dataType: {
    type: String,
    required: true,
  },
  dataSample: {
    type: Object,
    required: true,
  },
  tableHeight: {
    type: String,
    default: "auto",
  },
})

const tableHeader = getTableHeaderByDataType(dataType)

</script>

<template>
  <Form class='data-sample'>
    <div class='field' v-if="dataSample.name">
      {{ dataSample.name }}
    </div>

    <div class='field' v-if="dataSample.timestamp">
      {{ dataSample.timestamp }}
    </div>

    <div class='field' v-if="dataSample.description">
      <div class='description'>
        {{ dataSample.description }}
      </div>
    </div>

    <Table class='data-table not-field' :maxHeight="tableHeight">
      <thead>
        <tr>
          <th>#</th>
          <th v-for="heading in tableHeader">{{ heading }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="record in dataSample.records">
          <td></td>
          <td>{{ record[0] }}</td>
          <td>{{ record[1] }}</td>
        </tr>
      </tbody>
    </Table>

  </Form> 
</template>

<style scoped lang="sass">

.field
  padding: 7px 12px
  display: inline !important
  background-color: #f6f6f6
  border-radius: 7px
  margin-bottom: 10px !important

  &:hover
    background-color: #eaeaea

.description
  word-break: all

  display: -webkit-box
  -webkit-line-clamp: 3
  -webkit-box-orient: vertical
  overflow: hidden
  text-overflow: ellipsis

.data-sample
  display: flex
  flex-direction: column
  align-items: flex-start

</style>
