function clicar(){
    let agora = new Date()
    let ano = agora.getFullYear()
    let anoDeNascimento = window.document.querySelector('input#anoDeNa').value
    let id = anoDeNascimento - ano
    let idade = id - id - id
    let imagem = window.document.querySelector('img#img')
    let texto = window.document.getElementById('h2')
    let sexoR = window.document.getElementsByName('sexo')
    if(idade < 120){
        for(let c = 0; c < sexoR.length; c++){
            if(sexoR[c].checked){
                let sexo = sexoR[c].value
                if(sexoR[c].value == ''){
                    alert('Marque qual e o seu sexo')
                }
                else{
                    if(idade >= 0 && idade <= 12){
                        texto.innerHTML = `Voce tem ${idade} anos, voce e uma criança`
                        imagem.src = 'children.png'
                    }
                    else if(idade > 13 && idade < 60 && sexo == 'Masculino'){
                            texto.innerHTML = `Voce tem ${idade} anos, voce e do sexo ${sexo}`
                            imagem.src = 'man.png'
                    } 
                    else if(idade > 13 && idade < 60 && sexo == 'Feminino'){
                        texto.innerHTML = `Voce tem ${idade} anos, voce e do sexo ${sexo}`
                        imagem.src = 'woman.png'
                    }
                    else if(idade >= 60 && sexo == 'Masculino'){
                        texto.innerHTML = `Voce tem ${idade} anos, voce e do sexo ${sexo}`
                        imagem.src = 'oldman.png'                
                    }
                    else if(idade >= 60 && sexo == 'Feminino'){
                        texto.innerHTML = `Voce tem ${idade} anos, voce e do sexo ${sexo}`
                        imagem.src = 'oldwoman.png'
                    }
                    
                }
            }
        }
    }
    else{
        alert('Digite corretamente seu ano de nascimento')
    }
}    

