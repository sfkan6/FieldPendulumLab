


export const downloadByHref = async (href, filename="test") => {
  let a = document.createElement('a');
  a.href = href
  a.download = filename;
  a.click();
  a.remove();
}


export const getContentByFile = async (file) => {
  let reader = new FileReader();
  reader.readAsText(file, 'UTF-8');
  return await new Promise(resolve => {
    reader.onload = () => resolve(reader.result)
  });
}

