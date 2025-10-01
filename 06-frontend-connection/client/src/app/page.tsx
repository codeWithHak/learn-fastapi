// --------------- Error handled Code Simple Connection ----------------------------

"use client"
import { useEffect, useState } from "react";


export default function Home() {
  const [msg, setMsg] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/hello")
      .then(res => {
        if (!res.ok) throw new Error(res.statusText);
        return res.json();
      })
      .then(data => setMsg(data.message))
      .catch(err => setMsg("Error: " + err.message));
  }, []);

  return <main><h1>From FastAPI: {msg ?? "loading..."}</h1></main>;
}




// ------------- Include another endpoint --------

// "use client"

// import {useEffect, useState} from "react"

// export default function Home() {
//   const [greet, setGreet] = useState("")
//   const [bye, setBye] = useState("")

//   useEffect(()=>{
//     fetch("http://127.0.0.1:8000/hello")
//     .then(res => res.json())
//     .then(data => setGreet(data))

//   },[])

//     useEffect(()=>{
//     fetch("http://127.0.0.1:8000/bye")
//     .then(res => res.json())
//     .then(data => setBye(data))

//   },[])


  
//   return <main>
//     <h1>Response: {greet}</h1>
//     <h1>Response: {bye}</h1>
//     </main>
// } 

