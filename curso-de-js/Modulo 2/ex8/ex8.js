function clicar(){
    let colorJs = window.document.querySelector('input#color').value
    let corpoJs = window.document.getElementsByTagName('body')[0]
    corpoJs.style.backgroundColor = colorJs
}