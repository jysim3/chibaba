import React from 'react';
import { Button, Icon, Form, Input, Checkbox } from 'antd';
import { useCookies } from 'react-cookie';
class LoginForm extends React.Component {
    handleSubmit = e => {

      e.preventDefault();
      this.props.form.validateFields((err, values) => {
          console.log("receive fields of ", values)
        if (!err) {
            fetch('http://localhost:5000/login', {
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
                    document.cookie = "username=" + values["username"]
                } else {
                    document.cookie = "username=anon"
                }
            })
            .catch(reason => console.log(reason));
        }
      });
    };
  
    render() {
      const { getFieldDecorator } = this.props.form;
      return (
        <Form onSubmit={this.handleSubmit} className="login-form">
          <Form.Item>
            {getFieldDecorator('username', {
              rules: [{ required: true, message: 'Please input your username!' }],
            })(
              <Input
                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                placeholder="Username"
              />,
            )}
          </Form.Item>
          <Form.Item>
            {getFieldDecorator('password', {
              rules: [{ required: true, message: 'Please input your Password!' }],
            })(
              <Input
                prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
                type="password"
                placeholder="Password"
              />,
            )}
          </Form.Item>
          <Form.Item>
            {getFieldDecorator('remember', {
              valuePropName: 'checked',
              initialValue: true,
            })(<Checkbox>Remember me</Checkbox>)}
            <a className="login-form-forgot" href="#hi">
              Forgot password
            </a>
            <Button type="primary" htmlType="submit" className="login-form-button">
              Log in
            </Button>
            Or <a href="register">register now!</a>
          </Form.Item>
        </Form>
      );
    }
  
  
}
const WrappedLoginForm = Form.create({ name: 'login' })(LoginForm);
export default WrappedLoginForm;