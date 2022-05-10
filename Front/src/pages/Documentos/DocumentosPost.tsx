import axios from "axios";
import { useState } from "react";
import ListDocuments from "../../components/ListDocuments";
import Nav from "../../components/Nav";

export default function DocumentosPost() {

    const [document, setDocument] = useState({
        tema: "",
        autor: "",
        area_conhecimento: "",
        fonte: "",
        file_path: ""
    })

    axios.interceptors.request.use(
        config => {
            config.headers.Authorization = 'Bearer ' + localStorage.getItem('token')
            return config
        },
        error => {
            return Promise.reject(error);
        }
    )

    function handleChange(e) {
        const {value, name} = e.target

        setDocument(prevValue => {
            if(name === 'tema'){
                return {
                    tema: value,
                    autor: prevValue.autor,
                    area_conhecimento: prevValue.area_conhecimento,
                    fonte: prevValue.fonte,
                    file_path: prevValue.file_path
                }
            } else if (name === 'autor'){
                return {
                    tema: prevValue.tema,
                    autor: value,
                    area_conhecimento: prevValue.area_conhecimento,
                    fonte: prevValue.fonte,
                    file_path: prevValue.file_path
                }
            } else if (name === 'area_conhecimento'){
                return {
                    tema: prevValue.tema,
                    autor: prevValue.autor,
                    area_conhecimento: value,
                    fonte: prevValue.fonte,
                    file_path: prevValue.file_path
                }
            } else if (name === 'fonte'){
                return {
                    tema: prevValue.tema,
                    autor: prevValue.autor,
                    area_conhecimento: prevValue.area_conhecimento,
                    fonte: value,
                    file_path: prevValue.file_path
                }
            } else {
                return {
                    tema: prevValue.tema,
                    autor: prevValue.fonte,
                    area_conhecimento: prevValue.area_conhecimento,
                    fonte: prevValue.fonte,
                    file_path: value
                }
            }
        })
    }

    function handleClick(e) {
        e.preventDefault()

        axios.post("http://localhost:5000/api/documentos", document)
        .then(response => console.log(response))
        .catch(reason => console.log(reason))
    }

    return(
        <>
            <Nav/>
            <div className="post-document">
                <h2>Novo documento</h2>
                <form method="post">
                    <label htmlFor="tema">Tema</label>
                    <input onChange={handleChange} type="text" name="tema" value={document.tema}/>

                    <label htmlFor="autor">Autor</label>
                    <input onChange={handleChange} type="text" name="autor" value={document.autor}/>

                    <label htmlFor="area_conhecimento">Área de conhecimento</label>
                    <input onChange={handleChange} type="text" name="area_conhecimento" value={document.area_conhecimento}/>

                    <label htmlFor="fonte">Fonte</label>
                    <input onChange={handleChange} type="text" name="fonte" value={document.fonte}/>

                    <label htmlFor="file_path">file_path do arquivo</label>
                    <input onChange={handleChange} type="text" name="file_path" value={document.file_path}/>

                    <button onClick={handleClick}>Adicionar</button>
                </form>
            </div>
        </>
    )
}