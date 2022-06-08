import * as React from "react";
import { List, Datagrid, TextField } from 'react-admin';

export const ItemList = () => (
    <List>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
            <TextField source="unit" />
            <TextField source="quantity" />
            <TextField source="manufacture_date" />
            <TextField source="expiry_date" />
            <TextField source="price" />
        </Datagrid>
    </List>
);