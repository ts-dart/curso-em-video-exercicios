function apertar(){
    //recebe os inputs
    let corpo = document.querySelector('body')
    let inicioJ = document.querySelector('input#inicio')
    let fimJ = document.querySelector('input#fim')
    let passoJ = document.querySelector('input#passo')
    let botao = document.getElementById('botao')
    let secao1 = document.getElementById('sec')
    let div1 = document.getElementById('cxs')

    //converte os inputs para numeros
    let inicio = Number(inicioJ.value)
    let fim = Number(fimJ.value)
    let passo = Number(passoJ.value)

    //tratar erros
    if(inicio == 0 || fim == 0 || passo == 0){
        alert('Digite os dados corretamente!')
    }
    else if(inicio == fim){
        alert('Digite os dados corretamente')
    }
    else if(passo <= 0){
        alert('Digite os dados corretamentes')
    }
    else{
        //cria elementos e atribui identificadores
        var secRes = document.createElement('section')
        secRes.setAttribute('id', 'secRes')
        var texRes = document.createElement('h2')
        texRes.setAttribute('id', 'texRes')

        var secRes2 = document.createElement('section')
        secRes2.setAttribute('id', 'secRes2')
        var texRes2 = document.createElement('h2')
        texRes2.setAttribute('id', 'texRes2')

        let botao2 = document.createElement('input')
        botao2.setAttribute('type', 'button')
        botao2.setAttribute('value', '\\/')
        botao2.setAttribute('id', 'botao2')
        botao2.addEventListener('click', apertar2)

        let inicioJ2 = document.createElement('input')
        inicioJ2.setAttribute('type', 'Number')
        inicioJ2.setAttribute('size', '3')
        inicioJ2.setAttribute('placeholder', 'segundo')
        inicioJ2.setAttribute('id', 'inicioJ2')

        let fimJ2 = document.createElement('input')
        fimJ2.setAttribute('type', 'Number')
        fimJ2.setAttribute('size', '3')
        fimJ2.setAttribute('placeholder', 'segundo')
        fimJ2.setAttribute('id', 'fimJ2')

        let passoJ2 = document.createElement('input')
        passoJ2.setAttribute('type', 'Number')
        passoJ2.setAttribute('size', '3')
        passoJ2.setAttribute('placeholder', 'segundo')
        passoJ2.setAttribute('id', 'passoJ2')

        //mostra a segunda section
        div1.replaceChild(inicioJ2, inicioJ)
        div1.replaceChild(fimJ2, fimJ)  
        div1.replaceChild(passoJ2,passoJ)    
        secao1.replaceChild(botao2, botao)
        corpo.appendChild(secRes)
        
        //crecendo
        if(inicio < fim){
            for(var c = inicio; c <= fim; c+=passo){
                texRes.innerText += `  ${c} \u{1F9D9}`
                secRes.appendChild(texRes)
            }
        }
        //diminuindo
        else{
            for(var c = inicio; c >= fim; c-=passo){
                texRes.innerText += ` ${c} \u{1F9D9}`
                secRes.appendChild(texRes)
            }
        }    
        
        //a parada
        corpo.appendChild(secRes)
    }
    
    function apertar2(){
        let inicio2 = Number(inicioJ2.value)
        let fim2 = Number(fimJ2.value)
        let passo2 =  Number(passoJ2.value)

        //crecendo
        if(inicio < fim){
            for(var c2 = inicio2; c2 <= fim2; c2+=passo2){
                texRes2.innerText += `  ${c2} \u{1F9D9}`
                secRes2.appendChild(texRes2)
            }
        }
        //diminuindo
        else{
            for(var c2 = inicio2; c2 >= fim2; c2-=passo2){
                texRes2.innerText += ` ${c2} \u{1F9D9}`
                secRes2.appendChild(texRes2)
            }
        }

        corpo.replaceChild(secRes2, secRes)
        alert(texRes2)
    }
}


