package org.example.client;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;
import org.example.stubs.Bank;
import org.example.stubs.BankServiceGrpc;

import java.io.IOException;

public class BankGrpcClient2 {
    public static void main(String[] args) throws IOException {
        ManagedChannel managedChannel = ManagedChannelBuilder.forAddress("localhost", 5555)
                .usePlaintext()
                .build();
        BankServiceGrpc.BankServiceStub asyncstub = BankServiceGrpc.newStub(managedChannel);
        Bank.ConvertCurrencyRequest request = Bank.ConvertCurrencyRequest.newBuilder()
                .setCurrencyFrom("DH").setCurrencyTo("USD").setAmount(6500).build();
        asyncstub.convert(request, new StreamObserver<Bank.ConvertCurrencyResponse>() {
            @Override
            public void onNext(Bank.ConvertCurrencyResponse convertCurrencyResponse) {
                System.out.println("**************************************");
                System.out.println(convertCurrencyResponse.toString());
                System.out.println("**************************************");
            }
            @Override
            public void onError(Throwable throwable) { System.out.println(throwable.getMessage()); }
            @Override
            public void onCompleted() { System.out.println("END"); }
        });
        System.out.println("......?");
        System.in.read();
    }}

