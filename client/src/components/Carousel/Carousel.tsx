import React from 'react';
import classnames from 'classnames';
import Title from '../Title/Title';
import './Carousel.scss';


interface CarouselProps {
    title?: string;
    margin: string;
    carouselId?: string;
    children: unknown;
}

class Carousel extends React.Component<CarouselProps> {
    public static defaultProps = {
        margin: 'm',
    };
    public render() {
        const { children, margin, title, carouselId } = this.props;
        const itemCn = classnames(
            'Carousel-Item',
            margin && `Carousel-Item_margin_${margin}`,
        );
        const url = carouselId ? `https://yandex.ru/efir?from=efir_touch&stream_active=theme&stream_publisher=${carouselId}` : undefined;

        return (
            <div className="Carousel">
                <div className="Carousel-Header">
                    {title && <Title url={url}>{title}</Title>}
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
