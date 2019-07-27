import React from 'react';
import './App.css';
import { Card, Descriptions } from 'antd';
import cookie  from "react-cookies";


class Profile extends React.Component {
    state = {
        userInfo: {}
    }
    componentWillMount() {
        fetch('http://localhost:5000/getusrInfo', {
            
            method: 'POST',
            body: JSON.stringify({userID: cookie.load('userID')}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json() )
        .then(j => this.setState({userInfo: j[0]}))
    }
    render() {
        console.log(this.state.userInfo)
        const items = this.state.userInfo ? Object.keys(this.state.userInfo).map((k, index) => (
            <Descriptions.Item key={index} label={k}>{this.state.userInfo[k]}</Descriptions.Item>
        )) : null;
        return (
        <Card title="Card title" hoverable	 bordered={false} style={{ width: '50%', margin: 'auto' }}>
            <Descriptions title="User Info" bordered>
            {items}
            </Descriptions>
        </Card>
        );
    }

}

export default Profile;