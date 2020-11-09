import React from 'react';
import { useHistory } from 'react-router-dom';

import "../../index.css";

import Fatec from '../../imagem/fatecsjc2.png';
import Visiona from '../../imagem/visiona.png';
import Github from '../../imagem/github.png';
import logo from '../../imagem/logo.png';

function Access() {

  const history = useHistory();

  return(
    <>
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
        
        <div class="entrar">
        </div>
        <div class="entrada">
            <h1> Bem-Vindo </h1>
            <h3>Selecione um Banco de Dados</h3>
            <select className="nomtab">
                <option></option>
            </select><br/><br/>
            <button className="criartabela"
            onClick={() => history.push('/tabela')}
            >
              Criar uma conexão
          </button>
          <a></a>

          <button className="criartabela"
          onClick={() => history.push('/upload')}
          
          >
              Confirmar
          </button>
          

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

        </div>8
    </>
    
  );
}

export default Access;