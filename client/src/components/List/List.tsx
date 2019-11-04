import React from 'react';
import './List.scss';
import Carousel from '../Carousel/Carousel';
import Card, { CardProps } from '../Card/Card';

export interface ListProps {
    cards: CardProps[];
    content: string;
    title: string;
}

const List = ({cards, content, title}: ListProps) => {
  return (
    <Carousel title={title} margin="s">
      {cards.map((card) => <Card card={card} content={content}/>)}
    </Carousel>
  );
};

export default List;
