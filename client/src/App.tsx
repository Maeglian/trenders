import React from 'react';
import {Provider} from 'react-redux';
import './App.scss';
import Header from './components/Header/Header';
import Categories from './components/Categories/Categories';
import store from './store/createStore';

import Trends from './components/Trends/Trends';
import { items } from './feed.json';
import { items as blogersItems } from './blogers.json';
import List from './components/List/List';

const dramas: any[] = items[3].includes;
const blogers: any[] = blogersItems[0].includes;

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <div className="App">
        <Header />
        <Categories />
        <div className="App-Content">
          <Trends />
          <List cards={blogers} title={blogersItems[0].title} content="blogers"/>
          <List cards={dramas} title={items[3].title} content="series"/>
        </div>
      </div>
    </Provider>

  );
};

export default App;
