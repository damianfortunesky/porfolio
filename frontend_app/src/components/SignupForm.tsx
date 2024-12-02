import React from 'react';
import Button from './Button';

const SignupForm = () => {
  return (
    <form className="bg-gray-800 text-white p-8 rounded-xl shadow-lg w-full max-w-sm space-y-6">
      <div className="flex justify-center">
        <span className="text-4xl font-bold text-pink-500">🌊</span>
      </div>
      <h1 className="text-center text-2xl font-bold">Crea una cuenta</h1>

      <div className="space-y-1">
        <label className="block text-sm font-medium text-gray-300">Nombre completo</label>
        <input
          type="text"
          placeholder="Nombre completo"
          className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500"
        />
      </div>

      <div className="space-y-1">
        <label className="block text-sm font-medium text-gray-300">Correo electrónico</label>
        <input
          type="email"
          placeholder="Correo electrónico"
          className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500"
        />
      </div>

      <div className="space-y-1">
        <label className="block text-sm font-medium text-gray-300">Contraseña</label>
        <input
          type="password"
          placeholder="Contraseña"
          className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500"
        />
      </div>

      <div className="space-y-1">
        <label className="block text-sm font-medium text-gray-300">Confirmar contraseña</label>
        <input
          type="password"
          placeholder="Confirmar contraseña"
          className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500"
        />
      </div>

      <Button
        type="submit"
        label="Registrarse"
        className="w-full bg-pink-500 hover:bg-pink-600"
      />

      <p className="text-center text-sm text-gray-400">
        ¿Ya tienes una cuenta?{' '}
        <a href="/login" className="text-pink-500 hover:underline">
          Inicia sesión
        </a>
      </p>
    </form>
  );
};

export default SignupForm;
