import React from 'react';
import { useState } from "react";

export default function Barra() {
  const [busqueda, setBusqueda] = useState('');

  function saludo() {
    console.log("Hola");
  }

  return (
    <div className="flex-0 flex flex-col w-full bg-base-300 h-full px-10 py-10 justify-between">
      <div className="flex flex-col gap-5">
        <h2 className="font-bold text-4xl mx-5">DeepEye</h2>
        <div className="flex flex-col gap-2">
          <label htmlFor="input">Búsqueda</label>
          <input
            type="text"
            placeholder="Escribe algo"
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
            className="input input-bordered w-full max-w-xs"
          />
        </div>
      </div>
      <div className="flex flex-col items-center">
        <button onClick={saludo} className="btn btn-primary w-full"> Buscar</button>
      </div>
    </div>
  );
}
