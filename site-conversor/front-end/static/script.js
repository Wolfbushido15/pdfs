document.getElementById("uploadForm").onsubmit = async function(event) {
  event.preventDefault();
  let formData = new FormData();
  formData.append("file", document.getElementById("pdfFile").files[0]);

  document.getElementById("status").innerText = "Enviando arquivo...";

  let response = await fetch("/", {
      method: "POST",
      body: formData
  });

  if (response.ok) {
      let blob = await response.blob();
      let url = window.URL.createObjectURL(blob);
      let a = document.createElement("a");
      a.href = url;
      a.download = "PDF_Traduzido.pdf";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      document.getElementById("status").innerText = "Download concluído!";
  } else {
      document.getElementById("status").innerText = "Erro ao traduzir.";
  }
};