import React from 'react';
import './App.css';
import { Card, Table } from 'antd';
import cookie from 'react-cookies';


class PurchaseHistory extends React.Component {
    
      
    componentWillMount() {
        const userID = cookie.load('userID');
        fetch('http://localhost:5000/purchaseHistory', {
            
            method: 'POST',
            body: JSON.stringify({userID: `${userID}`}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json() )
        .then(j => console.log(JSON.stringify(j)))
    }
    render() {
        const dataSource = [
            {
              key: '1',
              name: 'Mike',
              age: 32,
              address: '10 Downing Street',
            },
            {
              key: '2',
              name: 'John',
              age: 42,
              address: '10 Downing Street',
            },
          ];
          
          const columns = [
            {
              title: 'Name',
              dataIndex: 'name',
              key: 'name',
            },
            {
              title: 'Age',
              dataIndex: 'age',
              key: 'age',
            },
            {
              title: 'Address',
              dataIndex: 'address',
              key: 'address',
            },
          ];
        return (
        <Card title="Card title" hoverable	 bordered={false} style={{ width: '50%', margin: 'auto' }}>
        <Table columns={columns} dataSource={dataSource} />
        </Card>)
    }

}

export default PurchaseHistory;