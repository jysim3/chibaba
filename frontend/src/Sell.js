import React from 'react';
import { InputNumber, Card, Button, Upload, Form, Input, Icon, Select} from 'antd';

import cookie from 'react-cookies';
const { Option } = Select;
const { TextArea } = Input;

class Sell extends React.Component {
    state = {
        free: false,
        submit: '',
        uploading: false,
        fileList: []
    }
    handleSubmit = e => {
      e.preventDefault();
      this.props.form.validateFields((err, values) => {
        if (!err) {
            let data = values;
            data['userID'] = cookie.load('userID');
            data['files'] = this.state.fileList;

            fetch('http://localhost:5000/sellItem', {
                method: 'POST',
                body: JSON.stringify(values),
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
            .then(response => response.json())
            .then(j => {
                if (j.status === 200){
                    this.state.submit = 'success';
                    window.location.href = '/';
                    
                } 
            })
            .catch(reason => console.log(reason));
          console.log('Received values of form: ', values);
        }
      });
    };
  
    render() {
        const { free, fileList } = this.state;
        const { submit } = this.state;
        console.log(free)
      const { getFieldDecorator } = this.props.form;
      return (
        <Card title="Card title" hoverable	 bordered={false} style={{ width: '50%', margin: 'auto' }}>

        <Form onSubmit={this.handleSubmit} className="login-form">
          <Form.Item>
            {getFieldDecorator('name', {
              rules: [{ required: true, message: "Please input your item's name!" }],
            })(
              <Input
                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                placeholder="Item name"
              />,
            )}
          </Form.Item>
          <Form.Item>
                <Input.Group compact>
                    <Select defaultValue="$" >
                        <Option value="$">$</Option>
                        <Option value="free">free</Option>
                    </Select>
            {getFieldDecorator('price', {
              rules: [{ required: true, message: 'Please input your price!' }],
            })(
                
              <InputNumber
                step={0.5}
                disabled={free}
                placeholder="Price"
              />
              ,
            )}
            </Input.Group>
          </Form.Item>
          <Form.Item>
            {getFieldDecorator('description', {
              rules: [{ required: true, message: 'Please enter a description!' }],
            })(
              <TextArea rows={4} 
              prefix={<Icon type="dollar" style={{ color: 'rgba(0,0,0,.25)' }} />}
              placeholder="Description"/>
              ,
            )}
          </Form.Item>
          <Form.Item label="Upload" extra="">
            <Upload name="logo" listType="picture" beforeUpload={file => {
                    this.setState(state => ({
                        fileList: [...state.fileList, file],
                    }));                
                    return false;
                }} 
            >
              <Button>
                <Icon type="upload" /> Click to upload
              </Button>
            </Upload>
        </Form.Item>
        <Form.Item wrapperCol={{ span: 12, offset: 6 }}>
        
          <Button type="primary" htmlType="submit">
            Save world
          </Button>
        </Form.Item>
        </Form>
        </Card>

      );
    }
  
  
}
const SellForm = Form.create({ name: 'sell' })(Sell);
/*
name
price
description
photo
*/
export default SellForm;