package javabeans;

import javabeans.Empregado;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.7.10.v20211216-rNA", date="2022-07-11T15:38:54")
@StaticMetamodel(Departamento.class)
public class Departamento_ { 

    public static volatile SingularAttribute<Departamento, Integer> numero;
    public static volatile SingularAttribute<Departamento, String> nome;
    public static volatile SingularAttribute<Departamento, Long> id;
    public static volatile SingularAttribute<Departamento, Empregado> gerente;

}