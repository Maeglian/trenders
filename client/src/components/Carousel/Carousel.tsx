import React from 'react';
import classnames from 'classnames';
import Title from '../Title/Title';
import './Carousel.scss';


interface CarouselProps {
    title?: string;
    margin: string;
    children: unknown;
}

class Carousel extends React.Component<CarouselProps> {
    public static defaultProps = {
        margin: 'm',
    };
    public render() {
        const { children, margin, title } = this.props;
        const itemCn = classnames(
            'Carousel-Item',
            margin && `Carousel-Item_margin_${margin}`,
        );

        return (
            <div className="Carousel">
                <div className="Carousel-Header">
                    {title && <Title>{title}</Title>}
                    <div className="Carousel-Hide"></div>
                </div>
                <div className="Carousel-List">
                    {React.Children.map(children, (child, num) =>
                        <div className={itemCn} key={num}>{child}</div>)}
                </div>
            </div>
        );
    }
}

export default Carousel;
