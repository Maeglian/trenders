import React, { Component } from 'react';
import Carousel from '../Carousel/Carousel';
import './Categories.scss';


const categories = ['Что посмотреть', 'Фильмы', 'Сериалы', 'Мультфильмы', 'Блогеры', 'Спорт', 'Музыка', 'Игры'];

class Categories extends Component {
    render() {
        return (
            <div className="Categories">
                <Carousel>
                {
                    categories.map((item) => (
                        <div className="Categories-Item">
                            {item}
                        </div>
                    ))
                }
                </Carousel>
                
            </div>
        );
    }
}

export default Categories;