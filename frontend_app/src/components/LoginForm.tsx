import { useState } from 'react';
import Button from './Button'; 
import InputField from './InputField';
import FormLabel from './FormLabel';

const LoginForm = () => {
    
  const [formData, setFormData] = useState({
    user: "",
    password: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const payload = {
      username: formData.user,
      password: formData.password,
    };

    try {

      const response = await fetch('http://127.0.0.1:8000/auth/login', {
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body:JSON.stringify(payload),
      });
  
      if(response.ok) {
        const data = await response.json();
  
        console.log('Token de acceso:', data.access_token);
        localStorage.setItem('token', data.access_token); // Guardar token si es necesario

      } else {

        const errorData = await response.json();
        console.error('Error:', errorData);

      }

    } catch (error) {
      console.error('Error en la solicitud:', error);
    }
  };

  return (
    <form  onSubmit={handleSubmit} className="space-y-4">
      <FormLabel htmlFor="user" label="Usuario" />
      <InputField
        id="user"
        name="user"
        type="text"
        value={formData.user}
        onChange={handleChange}
        placeholder="Ingresa tu Usuario"
      />
      <FormLabel htmlFor="password" label="Contraseña" />
      <InputField
        id="password"
        name="password"
        type="password"
        value={formData.password}
        onChange={handleChange}
        placeholder="Ingresa tu contraseña"
      />
      <Button type="submit" label='Ingresar'/>
    </form>
  );
};
export default LoginForm;

