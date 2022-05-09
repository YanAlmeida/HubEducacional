import axios from "axios"
import { useState } from "react"


export default function UserForm(props) {
    const [name, setName] = useState("")
    const [user, setUser] = useState("")
    const [password, setPassword] = useState("")

    function changeLogin(e) {
        const {value, name} = e.target
        
        if(name === 'username'){
            setUser(value)
        } else if (name === 'password'){
            setPassword(value)
        } else {
            setName(value)
        }
    }
    
    function handleClick(e){
        if(props.action === 'Cadastrar'){
            
            const registration = {
                user: user,
                senha: password,
                nome: name,
                registro: 2
            }

            axios.post('http://localhost:5000/api/alunos', registration)        
            .then(response => window.location.href="/login")
            .catch(reason => console.log(reason))
        } else {

            const login = {
                user: user,
                senha: password
            }

            axios.post('http://localhost:5000/api/autenticar', login)
            .then(response => {
                window.localStorage.setItem('token' , response.data.token)
                window.location.href="/documentos"
            })
            .catch(reason => console.log(reason))
        }

        e.preventDefault()
    }

    return(        
        <form>
            {props.action==='Cadastrar' &&
                <div className="form-group">
                    <label>Nome</label>
                    <input  
                        className="form-control" 
                        name="name" 
                        onChange={changeLogin}
                        value={name}
                    />
                </div>
            }
            <div className="form-group">
                <label>Usuário</label>
                <input  
                    className="form-control" 
                    name="username" 
                    onChange={changeLogin}
                    value={user}
                />
            </div>

            <div className="form-group">
                <label htmlFor="password">Senha</label>
                <input 
                    type="password" 
                    className="form-control" 
                    name="password"
                    onChange={changeLogin}
                    value={password}
                />
            </div>

            <button onClick={handleClick} className="btn btn-dark">{props.action}</button>
        </form>
    )
}