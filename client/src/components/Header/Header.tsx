import React, { Component } from 'react';
import './Header.scss';
import Icon from '../Icon/Icon';
import { ReactComponent as Search } from '../../images/svg/search.svg';
import { ReactComponent as Logo } from '../../images/svg/logo.svg';

class Header extends Component {
    public render() {
        return (
            <div className="Header">
                <div className="Header-Logo">
                    <Logo />
                </div>
                <Icon className="Header-Search"><Search /></Icon>
            </div>
        );
    }
}

export default Header;
