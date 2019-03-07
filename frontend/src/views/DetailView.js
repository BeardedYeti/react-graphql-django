// File: ./frontend/src/views/DetailView.js

import React from 'react';
import { Query } from 'react-apollo';
import gql from 'graphql-tag';

export default class DetailView extends React.Component {
  render() {
    return (
      <Query query={ MESSAGE_QUERY } variables={{ id: this.props.match.params.id }}>
        {({ loading, error, data }) => {
          if (loading) return <span>Loading...</span>
          if (error) return <span>Error</span>
          return (
            <div>
              <h1>Message {data.message.id}</h1>
              <p>{data.message.creationDate}</p>
              <p>{data.message.message}</p>
            </div>
          )
        }}
      </Query>
    )
  }
};

const MESSAGE_QUERY = gql`
  query DetailView($id: ID!) {
    message(id: $id) {
      id,
      creationDate,
      message
    }
  }
`;
