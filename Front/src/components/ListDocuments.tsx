import axios from "axios";
import { useCallback, useState } from "react";
import DocCard from "./DocCard";

axios.interceptors.request.use(
    config => {
        config.headers.Authorization = 'Bearer ' + localStorage.getItem('token')
        return config
    },
    error => {
        return Promise.reject(error);
    }
)

export default function ListDocuments() {

    const [documents, setDocuments] = useState([])
    const [requestError, setRequestError] = useState([])

    try{
        axios.get("http://localhost:5000/api/documentos")
        .then(({data}) => setDocuments(data.data))
    } catch (err){
        setRequestError(err.message)
    }
      

    return(
        <div className="list-documents">
            <>
                <div className="docs-deck">
                    {documents.map(document => {
                        return <DocCard doc={document}/>
                    })}
                </div>
            </>
        </div>
    )
}