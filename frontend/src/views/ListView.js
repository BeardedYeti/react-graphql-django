// File: ./frontend/src/views/ListView.js

import React from 'react'
import { Link } from 'react-router-dom'
import { Query } from 'react-apollo'
import gql from 'graphql-tag'

const MESSAGES_QUERY = gql`
  {
    allMessages {
      id, message
    }
  }
`

const ListView = ({ refetch }) => (
  <Query
    query={MESSAGES_QUERY}
    fetchPolicy={refetch ? 'cache-and-network' : 'cache-first'}
  >
    {({ loading, data: { data.allMessages } }) => {
      if (loading) return <span>Loading...</span>
      return (
        <div>
          {allMessages.map(item => (
            <p key={item.id}>
              <Link to={`/messages/${item.id}/`}>
                {item.message}
              </Link>
            </p>
          ))}
        </div>
      )
    }}
  </Query>
)

export default ListView