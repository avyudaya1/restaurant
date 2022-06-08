import { List, Datagrid, TextField } from 'react-admin';

const MenuItemList = () => (
    <List>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
            <TextField source="ingredients" />
            <TextField source="cooking_time" />
            <TextField source="cost" />
            <TextField source="menu_category" />
        </Datagrid>
    </List>
);

export default MenuItemList;