


export const getColumns = (records, step=1) => {
  const numberOfColumns = records[0].length
  let columns = [...Array(numberOfColumns)].map(() => Array(0));

  for (let i = 0; i < records.length; i+=step) {
    for (let j = 0; j < numberOfColumns; j+=1) {
      columns[j].push(records[i][j])
    }
  }
  return columns
}
