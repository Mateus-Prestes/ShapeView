import React from 'react'
import { useHistory } from 'react-router-dom';

import "../../index.css";

import Fatec from '../../imagem/fatecsjc2.png';
import Visiona from '../../imagem/visiona.png';
import Github from '../../imagem/github.png';
import logo from '../../imagem/logo.png';

function Registro(){

    const history = useHistory();

    return(
    <div className="regitro">   
        <header class="menu-principal">
        <main>            
            <div class="header-1">
                <div class="logo">
                    <ul>
                        <li>
                        <button className='fatec'>
                            <img src={Fatec} />
                        </button>
                        </li>
                        <li>
                            <button className='visiona'>
                                <img src={Visiona}/>
                            </button>
                        </li>
                    </ul>

                </div>
                    <div class="linkgit">
                    
                    <button className='github'>
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
        <main>
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
            <fieldset>
                <legend>Registro</legend>
                <form name="form">
                    Nome: <input class="nomer" type="text" name="Nome" autocomplete="off"/><br/><br/>
                    senha: <input class="senhar" type="password" name="Senha" autocomplete="off"/><br/><br/>
                    email: <input class="emailr" type="text" name="Email" autocomplete="off"/><br/><br/>

                    <button
                    onClick={() => history.push('/')}
                    >
                        Enviar
                    </button>

                    <button
                    onClick={() => history.push('/registro')}
                    >
                        Limpar
                    </button>

                </form>
            </fieldset> 
            </div>
        </main>
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
    )
}

export default Registro;