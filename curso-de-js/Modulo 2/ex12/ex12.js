function carregar(){
    let corpo = document.querySelector('body')
    let a = new Date()
    let agora = a.getHours()

    if(agora >= 6 && agora < 12 ){
        var hora = `Ola bom dia, vamos contar!`
        corpo.style.backgroundColor = 'gold'
    }
    else if(agora >= 12 && agora < 18){
        var hora = `Ola boa tarde, vamos contar!`
        corpo.style.backgroundColor = 'darkorange'
    }
    else{
        var hora = `Ola boa noite, vamos contar!`
        corpo.style.backgroundColor = 'darkblue'
    }
    
    //cabecalho
    let cabecalho = document.createElement('header')
    cabecalho.setAttribute('id', 'cabecalho')

    let saudacao = document.createElement('h1')
    saudacao.setAttribute('id', 'saudacao')
    saudacao.innerHTML = `${hora}`

    cabecalho.appendChild(saudacao)
    corpo.appendChild(cabecalho)

    //primeira secao
    let secaoPrincial = document.createElement('section')
    secaoPrincial.setAttribute('id', 'secaoprincipal')

    let texto = document.createElement('h2')
    texto.setAttribute('id', 'texto')
    texto.innerHTML = `Digite um numero e veja sua tabuada!`

    let caixa = document.createElement('input')
    caixa.setAttribute('type', 'number')
    caixa.setAttribute('size', '4')
    caixa.setAttribute('placeholder', '\u{1F609}')
    caixa.setAttribute('id', 'caixa')

    let botao = document.createElement('input')
    botao.setAttribute('type', 'button')
    botao.setAttribute('value', '\u{2714}')
    botao.setAttribute('id', 'botao')
    botao.addEventListener('mouseenter', entrar)
    botao.addEventListener('mouseout', sair)
    botao.addEventListener('click', clicar)

    function sair(){
        botao.style.backgroundColor = 'tomato'
    }

    function entrar(){
        botao.style.backgroundColor = 'brown'
    }

    function clicar(){
        let cx = Number(caixa.value)

        if(cx < 0){
            alert('Digite um numero positivo')
        }
        else if(cx == ''){
            alert('Voce ainda nao digitou nada!')
        }
        else{
            //segunda secao
            let secao = document.createElement('section')
            secao.setAttribute('id', 'secao')

            //cria a resposta
            let resultado1 = document.createElement('p')
            resultado1.setAttribute('id', 'resultado1')

            let resultado2 = document.createElement('p')
            resultado2.setAttribute('id', 'resultado2') 

            let resultado3 = document.createElement('p')
            resultado3.setAttribute('id', 'resultado3')

            let resultado4 = document.createElement('p')
            resultado4.setAttribute('id', 'resultado4')

            //cria div
            let divisao1 = document.createElement('div')
            divisao1.setAttribute('id', 'divisao1')

            let divisao2 = document.createElement('div')
            divisao2.setAttribute('id', 'divisao2')

            let divisao3 = document.createElement('div')
            divisao3.setAttribute('id', 'divisao3')

            let divisao4 = document.createElement('div')
            divisao4.setAttribute('id', 'divisao4')

            //cria titulos
            let titulos1 =  document.createElement('p')
            titulos1.setAttribute('id', 'titulos1')
            titulos1.innerHTML = 'Soma'

            let titulos2 = document.createElement('p')
            titulos2.setAttribute('id', 'titulos')
            titulos2.innerHTML = 'Subtração'

            let titulos3 = document.createElement('p')
            titulos3.setAttribute('id', 'titulos3')
            titulos3.innerHTML = 'Divisão'

            let titulos4 = document.createElement('p')
            titulos4.setAttribute('id', 'titulos4')
            titulos4.innerHTML = 'Mutiplicação'

            //calculos
            let n = document.querySelector('input#caixa')
            let numero = Number(n.value)
           
            //soma
            for(var c1 = 0; c1 <= 10; c1++){
                divisao1.appendChild(titulos1)
                let rr1 = c1 + numero
                let r1 = Number.parseInt(rr1)
                resultado1.innerHTML += `${numero} + ${c1} = ${r1} <br>`
            }

            //subtração
            for(var c2 = 0; c2 <= 10; c2++){
                divisao2.appendChild(titulos2)
                let r = c2 - numero
                let rr2 = r - r - r
                let r2 = Number.parseInt(rr2)
                resultado2.innerHTML += `${numero} - ${c2} = ${r2} <br>`
            }

            //divisao
            for(var c3 = 0; c3 <= 10; c3++){
                divisao3.appendChild(titulos3)
                let rr3 = c3 / numero
                let r3 = Number.parseInt(rr3)
                resultado3.innerHTML += `${numero} % ${c3} = ${r3} <br>`
            }

            //mutiplicação
            for(var c4 = 0; c4 <= 10; c4++){
                divisao4.appendChild(titulos4)
                let rr4 = c4 * numero
                let r4 = Number.parseInt(rr4)
                resultado4.innerHTML += `${numero} * ${c4} = ${r4} <br> `
            }

            //repetir
            let tex = document.createElement('p')
            tex.setAttribute('id', 'tex')
            tex.innerHTML = 'Click no botao para repetir'

            let divisaoRepTex = document.createElement('div')
            divisaoRepTex.setAttribute('id', 'divisaorep')

            let divisaoRepBot = document.createElement('div')
            divisaoRepBot.setAttribute('id', 'divisaorepbot')

            let repetir = document.createElement('input')
            repetir.setAttribute('type', 'button')
            repetir.setAttribute('id', 'button')
            repetir.setAttribute('value', '\u{1F504}')
            
            //rodape2
            let rodape2 = document.createElement('footer')
            rodape2.setAttribute('id', 'rodape2')

            let paragrafo2 = document.createElement('p')
            paragrafo2.setAttribute('id', 'paragrafo2')
            paragrafo2.innerHTML = `&copy;By Thiago`

            //insere no corpo
            rodape2.appendChild(paragrafo2)
            divisaoRepTex.appendChild(tex)
            divisaoRepBot.appendChild(repetir)
            divisao1.appendChild(resultado1)
            divisao2.appendChild(resultado2)
            divisao3.appendChild(resultado3)
            divisao4.appendChild(resultado4)
            secao.appendChild(divisao1)
            secao.appendChild(divisao2)
            secao.appendChild(divisao3)
            secao.appendChild(divisao4)
            corpo.removeChild(rodape)
            corpo.appendChild(divisaoRepBot)
            corpo.appendChild(divisaoRepTex)
            corpo.appendChild(rodape2)
            corpo.replaceChild(secao, secaoPrincial)

            repetir.addEventListener('click', rep)
            function rep(){
                document.location.reload(true)
            }
        }
    }
    secaoPrincial.appendChild(texto)
    secaoPrincial.appendChild(caixa)
    secaoPrincial.appendChild(botao)
    corpo.appendChild(secaoPrincial)

    //rodape
    let rodape = document.createElement('footer')
    rodape.setAttribute('id', 'rodape')

    let paragrafo = document.createElement('p')
    paragrafo.setAttribute('id', 'paragrafo')
    paragrafo.innerHTML = `&copy;By Thiago`

    rodape.appendChild(paragrafo)
    corpo.appendChild(rodape)
}
