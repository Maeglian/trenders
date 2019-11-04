import React, { Component } from 'react';
import './Title.scss';

export default class Title extends Component {
    public render() {
        return <div className="Title">{this.props.children}</div>;
    }
}
