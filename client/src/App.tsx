import React from 'react';
import './App.scss';
import Header from './components/Header/Header';
import Categories from './components/Categories/Categories';

const App: React.FC = () => {
  return (
    <div className="App">
      <Header />
      <Categories />
    </div>
  );
};

export default App;
