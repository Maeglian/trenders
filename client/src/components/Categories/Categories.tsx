import React, { Component } from 'react';
import './Categories.scss';


const categories = ['Что посмотреть', 'Фильмы', 'Сериалы'];

class Categories extends Component {
    render() {
        return (
            <div className="Categories">
                {
                    categories.map((item) => (
                        <div className="Categories-Item">
                            {item}
                        </div>
                    ))
                }
            </div>
        );
    }
}

export default Categories;