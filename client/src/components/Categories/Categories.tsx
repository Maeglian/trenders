import React, { Component } from 'react';
import Carousel from '../Carousel/Carousel';
import './Categories.scss';


const categories = ['Что посмотреть', 'Фильмы', 'Сериалы', 'Мультфильмы', 'Блогеры', 'Спорт', 'Музыка', 'Игры'];

class Categories extends Component {
    render() {
        return (
            <Carousel list={categories}/>
        );
    }
}

export default Categories;