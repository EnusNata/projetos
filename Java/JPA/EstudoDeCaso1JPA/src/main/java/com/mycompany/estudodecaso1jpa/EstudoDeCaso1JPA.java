package com.mycompany.estudodecaso1jpa;

import DAO.EmpregadoDAO;
import java.util.ArrayList;
import java.util.List;
import javabeans.Departamento;
import javabeans.Empregado;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class EstudoDeCaso1JPA {

    public static void main(String[] args) {
        
        // VERIFICANDO AS FUNCIONALIDADES
        
        /*
        
        Empregado empregado = new Empregado(1L,"nathan","70096357495","jacarezinho");
        Departamento departamento = new Departamento(1L,"financeiro",1,empregado);
        
        EntityManagerFactory factory = Persistence.createEntityManagerFactory("EstudoDeCaso1-PU");
        EntityManager manager = factory.createEntityManager();
        
        EntityTransaction transaction = manager.getTransaction();
        
        transaction.begin();
        manager.merge(empregado);
        transaction.commit();
        
        transaction.begin();
        manager.merge(departamento);
        transaction.commit();
        
        manager.close();
        factory.close();
        
        funcionou
        
        */
        
        
        /* SALVAR
        
        Empregado empregado = new Empregado(2L,"naruto","70096657791","konoha");
        
        EmpregadoDAO empregadoDAO = new EmpregadoDAO();
        
        empregadoDAO.salvar(empregado);
        
        funcionou
        
        */
        
        
        //  ABRIR
        
        /*
        Empregado empregado = new Empregado();
        EmpregadoDAO empregadoDAO = new EmpregadoDAO();
        
        empregado = (Empregado) empregadoDAO.abrir(1L);
        System.out.println(empregado);
        
        funcionou
        
        */
        
        //  LISTAR
        
        /*
        Empregado empregado = new Empregado();
        EmpregadoDAO empregadoDAO = new EmpregadoDAO();
        List<Empregado> empregados = new ArrayList<>();
        
        empregados = empregadoDAO.listar(empregado);
        
        for(Empregado empregadogenerico : empregados){
            System.out.println(empregadogenerico);
        }
        
        funcionou
        
        */
 
        // REMOVER
        
        /*
        Empregado empregado = new Empregado(2L,"naruto","70096657791","konoha");
        EmpregadoDAO empregadoDAO = new EmpregadoDAO();
        
        System.out.println(empregadoDAO.remover(2L));
        
        funcionou
        
        */
        
        // SALVAR
        
        
        /*
        Empregado empregado = new Empregado(3L,"sasuke","44444444444","vila do som");
        EmpregadoDAO empregadoDAO = new EmpregadoDAO();
        
        System.out.println(empregadoDAO.salvar(empregado));
        
        funcionou
        
        */
        
    }
    
}
