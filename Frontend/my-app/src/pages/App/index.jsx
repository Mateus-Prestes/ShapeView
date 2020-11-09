import React from 'react'
import {useHistory} from 'react-router-dom';

import "../../index.css";

import Fatec from '../../imagem/fatecsjc2.png';
import Visiona from '../../imagem/visiona.png';
import Github from '../../imagem/github.png';
import logo from '../../imagem/logo.png';

function App() {
    const history = useHistory()
    return (
    <div className="App">
        <header class="menu-principal">
            <main>            
                <div class="header-1">
                    <div class="logo">
                        <ul>
                            <li>
                                <button 
                                className='fatec'
                                onClick={() => window.open( 'https://fatecsjc-prd.azurewebsites.net')}
                                >

                                  <img src={Fatec} />
                                  
                                </button>
                                
                                
                            </li>
                            <li>
                                <button 
                                className='visiona'
                                onClick={() => window.open( 'https://fatecsjc-prd.azurewebsites.net')}
                                >
                                  <img src={Visiona}/>

                                </button>
                            </li>
                        </ul>

                    </div>
                    <div class="linkgit">
                    
                        <button 
                        className='github'
                        onClick={() => window.open( 'https://github.com/Mateus-Prestes/Projeto-integrador-3-Semestre')}
                        >

                          <img src={Github}/>

                        </button>
                    
                    </div>
                </div>

            </main>

        </header>
        <main>
            <div class="header-2">


            </div>
        </main>

        <div class="entrar">
            <ul>
                <button
                className="sing-in"
                onClick={() => history.push('/')}
                >
                    Entrar
                </button>

                <button
                className="register-btn"
                onClick={() => history.push('/registro')}
                >
                    Registrar
                </button>

            </ul>
        </div>
        <div class="entrada">
        <h2> Preencha com o nome e a senha</h2>
        <fieldset className="arq">
            <legend>Login</legend>
            <form name="form">
                Nome: <input class= "nome" type="text" name="Nome" autocomplete="off"/><br/><br/>
                senha: <input class= "senha" type="password" name="Senha" autocomplete="off"/><br/><br/>

                <button
                onClick={() => history.push('/principal')}
                >
                    Enviar
                </button>

                <input type="reset" name="limpar" value="Limpar" />

            </form>
        </fieldset>
        </div>
        <div className="logono">
            <ul>
                <img src={logo}/>
            </ul>
            <ul>
                <span className="span">
                    <font className="font1">ShapeView</font> 
                    Seu shapefile rápido e fácil
                </span>
            </ul>

        </div>
    </div>
  );
}

export default App;
