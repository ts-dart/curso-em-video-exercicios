var divisao = document.querySelector('div#div')
var selecao = document.querySelector('select#selecao')
var opcao = document.createElement('option')
var vf = []

function clicar(){
    var cx1 = document.querySelector('input#cx1')
    var numero = Number(cx1.value)

    if(isNaN(numero) || numero == ''){
        alert('Digite um numero!')
        cx1.value = ''
        cx1.focus()
    }
    else if(numero < 1 || numero > 100){
        alert('Digite um numero entre 1 e 100')
        cx1.value = ''
        cx1.focus()
    }
    else{
        vf.push(numero)
        cx1.value = ''
        cx1.focus()

        opcao = document.createElement('option')
        opcao.innerHTML = `Valor ${numero} adicionado`

        selecao.appendChild(opcao)
    }

    return v
}

function total(vf){
    for(var c = 0; c <= vf.length; c++){
        var totalNum = c
    }
    return totalNum
}

function maiorValor(vf){
    var maior = 0
    for(var c = 0; c < vf.length; c++){
        if(vf[c] > maior){
            maior = vf[c]
        }
    }    
    return maior
}

function menorValor(vf){
    var menor = vf[0]
    for(var c in vf){
        if(vf[c] < menor){
            menor = vf[c]
        }
    }
    return menor
} 

function somando(vf){
    var soma = 0
    for(var c = 0; c < vf.length; c++){
        var soma = soma + vf[c] 
    }
    return soma
}

function clicar2(){

    if(vf.length == ''){
        alert('Voce ainda nao digitou nada!')
    }
    else{
        if(somando(vf) != '' || somando(vf) != 0){
            var s = somando(vf)
            var t = total(vf)   
            var media  = s / t
        }

        var div2 = document.createElement('div')
        div2.setAttribute('id','div2')

        var tx1 = document.createElement('p')
        tx1.setAttribute('id', 'tx1')
        tx1.innerHTML = `Ao todo, ${total(vf)} numeros foram cadastrados.`

        var tx2 = document.createElement('p')
        tx2.setAttribute('id', 'tx2')
        tx2.innerHTML = `O maior valor informado foi ${maiorValor(vf)}.`

        var tx3 = document.createElement('p')
        tx3.setAttribute('id', 'tx3')
        tx3.innerHTML = `O menor valor informado foi ${menorValor(vf)}.`

        var tx4 = document.createElement('p')
        tx4.setAttribute('id', 'tx4')
        tx4.innerHTML = `Somando todos os valores, temos ${somando(vf)}.`

        var tx5 = document.createElement('p')
        tx5.setAttribute('id', 'tx5')
        tx5.innerHTML = `A media dos valores digitados e. ${media}`

        divisao.style.height = '450px'

        div2.appendChild(tx1)
        div2.appendChild(tx2)
        div2.appendChild(tx3)
        div2.appendChild(tx4)
        div2.appendChild(tx5)
        divisao.appendChild(div2)

        var cx = document.querySelector('input#cx1')
        cx.addEventListener('click', caixa1)

        function caixa1(){
            divisao.removeChild(div2)
            divisao.style.height = '330px'
            
            for(var r = selecao.length-1; r >= 0; r--){
                selecao[r] = null
            }
        }    
    }
}
