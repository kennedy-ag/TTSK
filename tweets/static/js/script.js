function limpar(){
	let barra = document.getElementById('busca');
	barra.value = '';
	barra.focus();
}

function adicionar_classe() {
  var element = document.getElementById("busca");
  element.classList.add("shadow-lg");
}

function alternar_classe() {
  var element = document.getElementById("busca");
  element.classList.remove("shadow-lg");
  element.classList.add("shadow-sm");
}