import React from 'react';
import { Card, Button, Upload, Form, Input, Icon, Select} from 'antd';
const { Option } = Select;
const { TextArea } = Input;
class Sell extends React.Component {
    state = {
        free: false
    }

    handleSubmit = e => {
      e.preventDefault();
      this.props.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    };
  
    render() {
        const { free } = this.state;
        console.log(free)
      const { getFieldDecorator } = this.props.form;
      return (
        <Card title="Card title" hoverable	 bordered={false} style={{ width: '50%', margin: 'auto' }}>

        <Form onSubmit={this.handleSubmit} className="login-form">
          <Form.Item>
            {getFieldDecorator('itemName', {
              rules: [{ required: true, message: "Please input your item's name!" }],
            })(
              <Input
                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                placeholder="Item name"
              />,
            )}
          </Form.Item>
          <Form.Item>
            {getFieldDecorator('price', {
              rules: [{ required: true, message: 'Please input your price!' }],
            })(
              <Input 
                addonBefore={(
                    <Select defaultValue="$">
                        <Option value="$">$</Option>
                        <Option value="free">free</Option>
                    </Select>
                )}
                disabled={free}
                prefix={<Icon type="dollar" style={{ color: 'rgba(0,0,0,.25)' }} />}
                placeholder="Price"
              />
              ,
            )}
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
          {getFieldDecorator('upload', {
            valuePropName: 'fileList',
            getValueFromEvent: this.normFile,
          })(
            <Upload name="logo" action="/upload.do" listType="picture">
              <Button>
                <Icon type="upload" /> Click to upload
              </Button>
            </Upload>,
          )}
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