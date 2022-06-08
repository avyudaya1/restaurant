import { List, Datagrid, TextField } from 'react-admin';

const CategoryList = () => (
    <List>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
        </Datagrid>
    </List>
);

export default CategoryList;