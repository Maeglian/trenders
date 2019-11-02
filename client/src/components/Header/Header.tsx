import React, { Component } from 'react';
import './Header.scss';
import Icon from '../Icon/Icon';
import  { ReactComponent as Search }  from '../../images/svg/search.svg';

class Header extends Component {
    render() {
        return (
            <div className="Header">
                <div className="Header-Logo">
                    <span className='Ya-Logo'>Яндекс</span> Эфир
                </div>
                <Icon><Search /></Icon>
            </div>
        );
    }
}

export default Header;