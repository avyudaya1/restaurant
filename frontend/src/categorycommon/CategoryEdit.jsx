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

const CategoryEdit = () => (
    <Edit>
        <SimpleForm>
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
);

export default CategoryEdit;