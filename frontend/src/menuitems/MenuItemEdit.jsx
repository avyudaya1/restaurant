import * as React from "react";
import {
    List,
    Datagrid,
    TextField,
    ReferenceField,
    EditButton,
    Edit,
    SimpleForm,
    ReferenceInput,
    SelectInput,
    NumberInput,
    TextInput,
    DateInput,
} from 'react-admin';

const MenuItemEdit = () => (
    <Edit>
        <SimpleForm>
            <TextInput source="id" />
            <TextInput source="name" />
            <TextInput source="ingredients" />
            <TextInput source="cooking_time" />
            <NumberInput source="cost" />
            <TextInput source="menu_category" />
        </SimpleForm>
    </Edit>
);

export default MenuItemEdit;